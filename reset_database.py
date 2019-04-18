from app import db

print("[INFO] Dropping Database Entries...")
db.drop_all()
print("[+] Successfully dropped!")

print("[INFO] Recreating Database Models...")
db.create_all()
print("[+] Successfully created!")

