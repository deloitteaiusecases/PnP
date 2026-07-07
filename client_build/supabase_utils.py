"""
supabase_utils.py — Supabase Storage integration for Policy & Procedure Agent.
Place this file in the same folder as app.py.
"""
import os
import tempfile
from pathlib import Path


def _client():
    from supabase import create_client
    from config import SUPABASE_URL, SUPABASE_KEY
    return create_client(SUPABASE_URL, SUPABASE_KEY)


def upload_file_to_supabase(file_bytes: bytes, filename: str, bucket: str) -> str:
    """Upload a file to Supabase Storage. Returns filename on success."""
    client = _client()
    try:
        # Try upload first
        client.storage.from_(bucket).upload(
            path=filename,
            file=file_bytes,
            file_options={"content-type": "application/octet-stream", "upsert": "true"}
        )
    except Exception as e:
        # If file exists, update it
        if "already exists" in str(e).lower() or "duplicate" in str(e).lower():
            client.storage.from_(bucket).update(
                path=filename,
                file=file_bytes,
                file_options={"content-type": "application/octet-stream"}
            )
        else:
            raise e
    return filename


def list_supabase_files(bucket: str) -> list:
    """
    List all DOCX and PDF files in the Supabase bucket.
    Returns list of dicts: [{name, size_mb, last_modified}]
    """
    client = _client()
    try:
        files = client.storage.from_(bucket).list()
        result = []
        for f in files:
            name = f.get("name", "")
            if name.lower().endswith((".docx", ".pdf")):
                size_bytes = f.get("metadata", {}).get("size", 0) if f.get("metadata") else 0
                updated_at = f.get("updated_at", "")[:16].replace("T", " ") if f.get("updated_at") else ""
                result.append({
                    "name":          name,
                    "size_mb":       round(size_bytes / (1024 * 1024), 2) if size_bytes else 0,
                    "last_modified": updated_at,
                })
        return sorted(result, key=lambda x: x["last_modified"], reverse=True)
    except Exception as e:
        print(f"[supabase] list error: {e}")
        return []


def download_supabase_file(filename: str, bucket: str) -> str:
    """
    Download a file from Supabase to a local temp file.
    Returns the temp file path. Caller must delete it after use.
    """
    client  = _client()
    data    = client.storage.from_(bucket).download(filename)
    suffix  = Path(filename).suffix.lower()
    fd, tmp = tempfile.mkstemp(suffix=suffix)
    os.close(fd)
    with open(tmp, "wb") as f:
        f.write(data)
    return tmp


def delete_supabase_file(filename: str, bucket: str) -> bool:
    """Delete a file from Supabase Storage. Returns True if successful."""
    try:
        _client().storage.from_(bucket).remove([filename])
        return True
    except Exception as e:
        print(f"[supabase] delete error: {e}")
        return False


def test_supabase_connection(bucket: str) -> tuple:
    """Test connection. Returns (success: bool, message: str)"""
    try:
        _client().storage.from_(bucket).list()
        return True, f"✅ Connected to Supabase bucket: {bucket}"
    except Exception as e:
        return False, f"❌ Cannot connect: {e}"