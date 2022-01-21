# Information

## Table of Matters

[Solution](#Solution)

[Resources](#Resources)

## Details

- **Points:** 10

- **Source:** picoCTF

- **Author:** SUSIE

## Description

Files can always be changed in a secret way. Can you find the flag? cat.jpg

### Hint 1

Look at the details of the file

### Hint 2

Make sure to submit the flag as picoCTF{XXXXX}

## Solution

- As usual, you need to download the image provided by the challenge using `wget` like so:

```
$ wget https://mercury.picoctf.net/static/d1375e383810d8d957c04eef9e345732/cat.jpg
```

PS: Right-click on the link and click on `copy link adress` to get the download URL.

- Right off the bat we see that it is a normal .jpg, there doesn't seem to be a flag directly on the image itself. The second hint indicates that we might want to look at the details of the image for some leads. Upon right-clicking the image and viewing its details, there doesn't seem to be anything out of the ordinary, so what does it mean?

- Another way to get the full details of an image is to inspect its EXIF data (Exchangeable Image File). Almost all new digital cameras use the EXIF annotation, storing information on the image. In our case, I suspect that someone might've altered the EXIF data of the photo after it was taken.

- We can inspect a photo's EXIF data either with online tools such as [exifdata.com](https://exifdata.com/) or locally with the package [exiftool](https://exiftool.org/install.html).

- Upon inspecting the EXIF data, I notice that the Licence value is weird. Is it just me or it looks encrypted ?

- Let's take a closer look at it ! From first glance I can tell that it's a `Base64` string. We can decrypt it to a Raw Format using online tools such as [CyberChef](https://gchq.github.io/CyberChef/).

And there we go, we found the flag !

## Resources

- [Metadata](https://en.wikipedia.org/wiki/Metadata/)

- [EXIF Data](https://en.wikipedia.org/wiki/Exif/)

- [Base64 Encoding](https://en.wikipedia.org/wiki/Base64)
