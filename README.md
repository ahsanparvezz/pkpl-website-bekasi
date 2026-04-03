Untuk file .env di hide menggunakan gitignore 

file .env berisikan

SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Google OAuth2 Credentials
# Dapatkan dari https://console.cloud.google.com/
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your-google-client-id.apps.googleusercontent.com
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your-google-client-secret

# Email anggota kelompok yang diizinkan mengubah tampilan
ALLOWED_MEMBER_EMAILS=anggota1@gmail.com,anggota2@gmail.com,anggota3@gmail.com
