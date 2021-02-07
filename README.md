# tvshow
Rename files with episode names

## Usage
Install requirements with `pip install -r requirements.txt`

### tvshow_folder_auto
`python tvshow_folder_auto.py <path>`

Provide path to tv show directory to automatically rename the files.

#### Examples
`The.Simpsons.S01E01.mkv` --> `The.Simpsons.S01E01.Simpsons.Roasting.on.an.Open.Fire.mkv`
`S01E02The.Simpsons.mkv` --> `The.Simpsons.S01E02.Bart.the.Genius.mkv`
`The.Simpsons.S01E03.aaa.bbb.ccc.mkv` --> `The.Simpsons.S01E03.Homer's.Odyssey.mkv`
`thesimpsonss01e04.mkv` --> `The.Simpsons.S01E04.There's.No.Disgrace.Like.Home.mkv`
`the_simpsons_s01e05.mkv` --> `The.Simpsons.S01E05.Bart.the.General.mkv`
