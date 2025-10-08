@@ -1,3 +1,34 @@
-import yt_dlp 
+import yt_dlp
 
\ No newline at end of file
-yt_dlp.YoutubeDL({'format': 'best','outtmpl':'%(title)s.%(ext)s'}).download(['https://www.youtube.com/live/A9Q25jJpGwY?si=3Buw6ZbvneMLDWcu'])
+# Prompt user for YouTube URL
+url = input("Enter YouTube URL: ")
+
+# Prompt user for format choice
+format_choice = input("Enter format (MP3 or MP4): ").strip().upper()
+
+if format_choice == 'MP3':
+    ydl_opts = {
+        'format': 'bestaudio/best',
+        'postprocessors': [{
+            'key': 'FFmpegExtractAudio',
+            'preferredcodec': 'mp3',
+            'preferredquality': '192',
+        }],
+        'outtmpl': '%(title)s.%(ext)s',
+    }
+elif format_choice == 'MP4':
+    ydl_opts = {
+        'format': 'best',
+        'outtmpl': '%(title)s.mp4',
+    }
+else:
+    print("Invalid format. Please choose MP3 or MP4.")
+    exit(1)
+
+# Download the video/audio
+try:
+    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
+        ydl.download([url])
+    print("Download completed successfully!")
+except Exception e:
+    print(f"An error occurred: {e}")