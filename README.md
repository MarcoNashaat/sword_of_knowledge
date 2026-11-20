# Sword of Knowledge

A three-player trivia strategy game (you vs two bots for now). Static site: no server needed.

## Files
- `index.html` - the complete game (questions are embedded, so it also works opened locally)
- `questions.json` - the question bank (edit this)
- `index.template.html` + `build.py` - run `python3 build.py` after editing questions.json to regenerate index.html
- `favicon.svg` - tab icon

## Deploy (free)
- **Cloudflare Pages**: Workers & Pages -> Create -> Pages -> Upload assets -> drop this folder (no build command, output = this folder).
- **GitHub Pages**: push these files to a repo, then Settings -> Pages -> Deploy from branch (main, / root).
- **Netlify**: drag this folder onto app.netlify.com/drop.

Status: prototype, draft question bank not yet fully fact-checked.
