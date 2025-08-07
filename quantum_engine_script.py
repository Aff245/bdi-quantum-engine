# quantum_engine_script.py (Versi Jenderal Tertinggi / ULTIMATE FINAL)

import os
from supabase import create_client, Client

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
if not SUPABASE_URL or not SUPABASE_KEY:
    print("❌ Error: Kredensial Supabase tidak ditemukan.")
    exit(1)
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def strategic_decision_engine(beliefs):
    print(f"🧠 Menganalisis Laporan Intelijen Lengkap (Mode Tertinggi): {beliefs}")

    # --- FASE 1: PENILAIAN INTELIJEN DENGAN BUKU PANDUAN ---
    
    # Pastikan 'beliefs' adalah format yang benar
    if not isinstance(beliefs, dict):
        print("   -> PERINGATAN: 'beliefs' yang diterima bukan format dictionary.")
        return {"next_action": "invalid_beliefs_format_received"}

    # BACA LAPORAN KESEHATAN (pastikan itu dictionary)
    system_health_report = beliefs.get("system_health", {})
    system_health_ok = isinstance(system_health_report, dict) and system_health_report.get("status") == "operational"
    
    # BACA LAPORAN PENGGUNA (pastikan itu dictionary)
    user_activity_report = beliefs.get("user_activity", {})
    active_users = user_activity_report.get("active_users_today", 0) if isinstance(user_activity_report, dict) else 0

    # BACA LAPORAN PENGEMBANGAN (INI KUNCINYA!)
    # Laporan GitHub datang sebagai [amplop berisi satu surat]. Kita buka dulu amplopnya.
    github_activity_report = beliefs.get("github_activity", [])
    development_activity_ok = isinstance(github_activity_report, list) and len(github_activity_report) > 0

    print(f"   -> Penilaian: Kesehatan OK? {system_health_ok}, Pengguna Aktif: {active_users}, Dev OK? {development_activity_ok}")

    # --- FASE 2: PENGAMBILAN KEPUTUSAN STRATEGIS ---
    if not system_health_ok:
        print("   -> KEPUTUSAN: Kesehatan sistem adalah prioritas #1!")
        return {"next_action": "initiate_self_healing_protocol"}

    if system_health_ok and active_users < 1000:
        print("   -> KEPUTUSAN: Kerajaan aman tapi sepi. Fokus pada pertumbuhan.")
        return {"next_action": "launch_user_acquisition_campaign"}

    if system_health_ok and active_users >= 1000 and development_activity_ok:
        print("   -> KEPUTUSAN: Kerajaan makmur! Waktunya untuk inovasi.")
        return {"next_action": "deploy_new_experimental_feature"}

    print("   -> KEPUTUSAN: Kondisi stabil. Lakukan optimisasi.")
    return {"next_action": "stabilize_and_optimize_core_systems"}

def process_pending_tasks():
    # ... Kode di bawah ini TIDAK PERLU DIUBAH sama sekali ...
    print("⚡ Memeriksa tugas baru di Supabase...")
    try:
        response = supabase.table('quantum_tasks').select('*').eq('status', 'pending').execute()
        if not response.data:
            print("...Tidak ada tugas 'pending' yang ditemukan. Selesai.")
            return
        for task in response.data:
            print(f"🔥 Mengerjakan tugas ID: {task['id']}...")
            try:
                # Kita tambahkan .get('payload') untuk keamanan ekstra
                result = strategic_decision_engine(task.get('payload', {}))
                supabase.table('quantum_tasks').update({'status': 'completed', 'result': result}).eq('id', task['id']).execute()
                print(f"✅ Tugas ID: {task['id']} selesai. Keputusan: {result.get('next_action')}")
            except Exception as e:
                print(f"❌ Error saat memproses tugas ID {task['id']}: {e}")
                supabase.table('quantum_tasks').update({'status': 'failed', 'result': {'error': str(e)}}).eq('id', task['id']).execute()
    except Exception as e:
        print(f"❌ Gagal terhubung atau mengambil data dari Supabase: {e}")

if __name__ == "__main__":
    process_pending_tasks()
