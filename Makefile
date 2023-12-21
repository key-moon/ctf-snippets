install: snippet.vsix
	code --install-extension dest/snippet.vsix

snippet.vsix: extension
	cd dest/extension; yes | vsce package -o ../snippet.vsix

extension:
	snipgen --config config.json --target vscode -- src dest/extension
