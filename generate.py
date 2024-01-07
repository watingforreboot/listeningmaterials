def generate_html_file(filename):
    html_content = f"""<!DOCTYPE html>
<html>
<body>

<audio id="audioPlayer" controls style="width: 100%;">
  <source src="{filename}.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

<button onclick="rewindAudio(3)" type="button" style="height: 90px; font-size: 50px; margin-top: 120px; touch-action: manipulation;">Rewind 3 seconds</button>

<script>
function rewindAudio(seconds) {{
  var audio = document.getElementById("audioPlayer");
  audio.currentTime -= seconds;
}}
</script>

</body>
</html>"""

    with open(f"{filename}.htm", 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)


def main():
    filename = input("Please enter a filename (without extension): ")
    generate_html_file(filename)


if __name__ == "__main__":
    main()
