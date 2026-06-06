# Telegram Redirect Service

Simple redirect server for Telegram file bots.

## Example

User opens:

```txt
https://your-koyeb-app.koyeb.app/watch/7189/file.zip?hash=AgADdR
```

Server redirects to:

```txt
https://your-heroku-app.herokuapp.com/watch/7189/file.zip?hash=AgADdR
```

---

# Deploy On Koyeb

## 1. Create GitHub Repository

Upload these files.

---

## 2. Create Koyeb Account

Official website:

```txt
https://app.koyeb.com/auth/signup
```

---

## 3. Create App

- Click `Create App`
- Choose `GitHub`
- Select repository
- Choose branch

---

## 4. Environment Variable

Add:

| Key | Value |
|-----|-----|
| BACKEND_URL | https://your-backend.herokuapp.com |

---

## 5. Port

Koyeb automatically detects port 8000.

---

## 6. Deploy

Press:

```txt
Deploy
```

After deployment:

```txt
https://your-app.koyeb.app
```

becomes your permanent redirect domain.

---

# Example Links

## Streaming

Input:

```txt
https://your-app.koyeb.app/watch/7189/file.zip?hash=AgADdR
```

Redirects to:

```txt
https://backend-app.herokuapp.com/watch/7189/file.zip?hash=AgADdR
```

---

## Download

Input:

```txt
https://your-app.koyeb.app/7189/file.zip?hash=AgADdR
```

Redirects to:

```txt
https://backend-app.herokuapp.com/7189/file.zip?hash=AgADdR
```

Browser/download manager will start download normally.

---

# Changing Backend Later

If Heroku/Koyeb app changes:

Just update:

```txt
BACKEND_URL
```

inside Koyeb environment variables.

No need to regenerate old Telegram links.

---

# Important Notes

This service only redirects.

It does NOT:
- store files
- proxy files
- cache files
- consume high bandwidth

So free tier usually works fine.
