pdfsuccess() {
  echo 'Uploading to haldean.org'
  scp resume.pdf haldean.org:/srv/static/
}

echo 'Generating LaTeX'
./resume.py latex programming.res \
    --pre_file templates/pre.tex \
    --post_file templates/post.tex \
    --output_file resumes/resume.tex

cd resumes
echo 'Generating PDF'
pdflatex resume.tex > /dev/null && pdfsuccess
