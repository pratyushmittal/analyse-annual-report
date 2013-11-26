FILENAME = "sample.pdf"
WORDS = ["shall", "should",
         "will", "would",
         "your company", "expects",
         "includ", "exclud", "adjust",
         "challenge", ]

from subprocess import call

def filter_lines():
    for i, blob in enumerate(get_blobs()):
        print "----{}---".format(i)
        print blob
        print "----{}---".format(i)


def to_tiff():
    call("convert -density 300 {0} -depth 8 {0}.tiff".format(FILENAME))


def to_text():
    call("tesseract {0}.tiff {0}.txt".format(FILENAME))


def get_blobs():
    # extract paragraphs
    # if word in paragraph
    # return line before and after
    with open(FILENAME + ".txt", "rb") as pdf:
        content = pdf.read()
    blobs = content.split("\n\n")
    for blob in blobs:
        if any(word in blob for word in WORDS):
            yield blob

filter_lines()
