# Hacklahoma 2023

## Inspiration
The theme for Hacklahoma 2023, "Empire Strikes Hack", provided an interesting starting point for our project brainstorming. The Star Wars universe is known for its futuristic technology, as well as rich lore, including several fictional languages from across the galaxy. Our project idea allowed us to explore this sci-fi technical aspect by conceptualizing, building, and decorating a handheld translation scanner.

## What it does
The Galactic Translator scans text written in Galactic Basic (also known as Aurebesh, the most common language in the Star Wars universe) when a physical button is pressed. The Translator then interprets the Aurebesh language, translates it to English, then reads the English translation aloud with text-to-speech using speakers built into the device.

## How we built it
When the activation button is pressed, a GPIO signal calls the translate function within a Python script stored on Raspberry Pi. This translate function uses OpenCV to access a USB webcam to photograph the text and save the image. This image is then processed by tesseract, an optical character recognition tool which our team trained to recognize Aurebesh characters as corresponding English characters. The informed tesseract library can then interpret the image as an English string, which we convert to lowercase to standardize responses. This string is passed into a gTTS (Google Text-to-Speech) object, which saves the text as an mp3 recording using the default female voice. Finally, this mp3 is played using mpg321 to play the audio aloud through connected USB speakers. If no text is found within the scan image, the device says "no text detected". Most of the hardware is contained within a small cardboard box, which we decorated with Star Wars iconography to match the theme.

## Challenges we ran into
We encountered a number of challenges in working with the hardware for this project. Our Raspberry Pi had a very outdated operating system version, and we needed to flash a new OS image onto the Pi's microSD card. Also, our Pi had an issue syncing the system clock, which was preventing package updates, so we had to manually correct the system time. Additionally, we had trouble loading the OpenCV module onto the PI due to various limitations, which took several hours to complete. Another ongoing challenge involved our difficulty in precisely aligning our sample printed Aurebesh text pages, so that the characters could be recognized with acceptable consistency. Our solution to this problem involved building a cardboard mount for the Aurebesh samples, which offered the stability and positional consistency needed for our OCR process.

## Accomplishments that we're proud of
Our device usually vocalizes the correct English translation, with occasional errors in individual characters within the word, which is a significant accomplishment considering the number of components involved. We are also proud that the device runs as a standalone hardware solution, with input, logic, and output being handled internally by the Raspberry Pi. 

## What we learned
This project gave all of our team members considerable experience working with popular tools that we had never before experienced in our academic coursework, namely computer vision with OpenCV and automated text to speech using gTTS. This also gave our team significant exposure to troubleshooting hardware issues, and working with a single-board computer. 

## What's next for Intergalactic Translation Device
There are a few improvements that could enhance our Translation Device. Currently our text scanning needs to have specific lighting, distance, and angle conditions for the OCR tool to process the characters accurately. Adding more training images to the Tesseract directory would help mitigate this problem, or we could alleviate this issue by adding postprocessing effects to the image, such as noise reduction or de-skewing to fix the initial image. Additionally, the use of a voice reader could allow for AI voice options to be added from characters across the Star Wars franchise. Finally, we could 3D print a casing for our device that would be more tailored for the components of our device than our current cardboard solution.
