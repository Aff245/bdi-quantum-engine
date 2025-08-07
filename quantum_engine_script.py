# quantum_engine_script.py (Versi Otak Ahli Strategi)

import os
import numpy as np
from supabase import create_client, Client

# ... (Bagian pengambilan kredensial Supabase tetap sama) ...
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
if not SUPABASE_URL or not SUPABASE_KEY:
    print("❌ Error: Kredensial Supabase tidak ditemukan.")
    exit(1)
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def strategic_decision_engine(beliefs):
    """
    Ini adalah Otak Kuantum yang sebenarnya. Ia membaca laporan intelijen
    dan membuat keputusan strategis berdasarkan kondisi kerajaan.
    """
    print(f"🧠 Menganalisis Laporan Intelijen: {beliefs}")

    # --- FASE 1: PENILAIAN KONDISI KERAJAAN ---
    
    # Cek Kesehatan Sistem (System Health)
    # Jika 'system_health' ada dan statusnya bukan 'unreachable' atau 'error'
    system_health_ok = 'system_health' in beliefs and beliefs['system_health'].get('status') not in ['unreachable', 'error']
    
    # Cek Aktivitas Pengguna (User Activity)
    # Jika 'user_activity' ada dan tidak error
    user_activity_ok = 'user_activity' in beliefs and beliefs['user_activity'].get('status') not in ['unreachable', 'error']

    # Cek Aktivitas Pengembangan (GitHub Activity)
    # Jika 'github_activity' tidak error (misalnya tidak 404)
    development_activity_ok = 'github_activity' in beliefs and beliefs['github_activity'].get('status') != 'error'

    print(f"   -> Penilaian: Kesehatan Sistem OK? {system_health_ok}, Aktivitas Pengguna OK? {user_activity_ok}, Aktivitas Dev OK? {development_activity_ok}")

    # --- FASE 2: PENGAMBILAN KEPUTUSAN STRATEGIS ---
    
    # PRIORITAS #1: Jika sistem tidak sehat, PERBAIKI DULU!
    if not system_health_ok:
        print("   -> KEPUTUSAN: Kesehatan sistem kritis! Fokus pada perbaikan.")
        return {"next_action": "initiate_self_healing_protocol"}

    # PRIORITAS #2: Jika sistem sehat tapi tidak ada aktivitas pengguna, CARI PENGGUNA!
    if system_health_ok and not user_activity_ok:
        print("   -> KEPUTUSAN: Sistem sehat tapi sepi. Fokus pada pertumbuhan.")
        return {"next_action": "launch_user_acquisition_campaign"}

    # PRIORITAS #3: Jika semua sehat, SAATNYA INOVASI!
    if system_health_ok and user_activity_ok and development_activity_ok:
        print("   -> KEPUTUSAN: Semua stabil. Waktunya untuk inovasi dan fitur baru.")
        return {"next_action": "deploy_new_experimental_feature"}

    # KONDISI DEFAULT: Jika tidak ada yang cocok, lakukan optimisasi.
    print("   -> KEPUTUSAN: Kondisi stabil. Lakukan optimisasi rutin.")
    return {"next_action": "stabilize_and_optimize_core_systems"}


def process_pending_tasks():
    # ... (Kode ini tidak perlu diubah sama sekali, karena ia hanya memanggil 'strategic_decision_engine') ...
    # ... ia akan mengambil tugas 'pending' dan memanggil fungsi di atas ...
    print("⚡ Memeriksa tugas baru di Supabase...")
    try:
        response = supabase.table('quantum_tasks').select('*').eq('status', 'pending').execute()
        if not response.data:
            print("...Tidak ada tugas 'pending' yang ditemukan. Selesai.")
            return

        for task in response.data:
            print(f"🔥 Mengerjakan tugas ID: {task['id']}...")
            try:
                result = {}
                if task.get('task_type') == 'optimize_desires':
                    # Panggil OTAK STRATEGIS kita yang baru
                    result = strategic_decision_engine(task['payload'])
                else:
                    result = {"next_action": "unknown_task_type_received"}

                supabase.table('quantum_tasks').update({'status': 'completed', 'result': result}).eq('id', task['id']).execute()
                print(f"✅ Tugas ID: {task['id']} selesai. Keputusan: {result.get('next_action')}")
            except Exception as e:
                print(f"❌ Error saat memproses tugas ID {task['id']}: {e}")
                supabase.table('quantum_tasks').update({'status': 'failed', 'result': {'error': str(e)}}).eq('id', task['id']).execute()
    except Exception as e:
        print(f"❌ Gagal terhubung atau mengambil data dari Supabase: {e}")

if __name__ == "__main__":
    process_pending_tasks()
