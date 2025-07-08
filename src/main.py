# src/main.py
from androguard.core.bytecodes.apk import APK

def analyze_apk(path):
    apk = APK(path)
    print(f"App Name: {apk.get_app_name()}")
    print(f"Package: {apk.get_package()}")
    print(f"Permissions: {apk.get_permissions()}")

if __name__ == "__main__":
    analyze_apk("sample.apk")  # Replace with actual APK path
