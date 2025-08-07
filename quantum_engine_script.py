# quantum_engine_script.py (Versi Jenderal Bijaksana - FINAL)

import os
from supabase import create_client, Client

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
if not SUPABASE_URL or not SUPABASE_KEY:
    print("❌ Error: Kredensial Supabase tidak ditemukan.")
    exit(1)
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def strategic_decision_engine(beliefs):
    """
    Versi ini jauh lebih tangguh dan tidak akan crash jika format data berbeda.
    """
    print(f"🧠 Menganalisis Laporan Intelijen Baru: {beliefs}")

    # --- FASE 1: PENILAIAN INTELIJEN SECARA HATI-HATI ---
    
    # --- PERUBAHAN KUNCI ---
    # Kita gunakan .get() berlapis untuk keamanan maksimal
    system_health_ok = beliefs.get("system_health", {}).get("status") == "operational"
    
    # Untuk aktivitas pengguna, kita anggap OK jika ada data 'active_users_today'
    user_activity_ok = "active_users_today" in beliefs.get("user_activity", {})
    active_users = beliefs.get("user_activity", {}).get("active_users_today", 0)

    # Untuk aktivitas dev, kita periksa status error
    development_activity_ok = beliefs.get("github_activity", {}).get("status") != "error"

    print(f"   -> Penilaian: Kesehatan OK? {system_health_ok}, Aktivitas Pengguna OK? {user_activity_ok}, Aktivitas Dev OK? {development_activity_ok}")
    print(f"   -> Data Pengguna Aktif: {active_users}")

    # --- FASE 2: PENGAMBILAN KEPUTUSAN STRATEGIS ---
    
    # PRIORITAS #1: Jika kesehatan sistem TIDAK OK, SEMBUHKAN!
    if not system_health_ok:
        print("   -> KEPUTUSAN: Kesehatan sistem adalah prioritas utama! Fokus pada perbaikan.")
        return {"next_action": "initiate_self_healing_protocol"}

    # PRIORITAS #2: Jika sistem sehat tapi aktivitas pengguna rendah
    if system_health_ok and active_users < 1000:
        print("   -> KEPUTUSAN: Kerajaan aman tapi sepi. Fokus pada kampanye pertumbuhan.")
        return {"next_action": "launch_user_acquisition_campaign"}

    # PRIORITAS #3: Jika semua sehat dan ramai, SAATNYA INOVASI!
    if system_health_ok and active_users >= 1000 and development_activity_ok:
        print("   -> KEPUTUSAN: Kerajaan makmur! Waktunya untuk fitur baru dan ekspansi.")
        return {"next_action": "deploy_new_experimental_feature"}

    # KONDISI DEFAULT: Jika kerajaan aman dan ramai, tapi dev tidak aktif, lakukan optimisasi.
    print("   -> KEPUTUSAN: Kondisi stabil. Lakukan optimisasi dan pemeliharaan rutin.")
    return {"next_action": "stabilize_and_optimize_core_systems"}


def process_pending_tasks():
    # ... (Kode di bawah ini tidak perlu diubah sama sekali) ...
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
