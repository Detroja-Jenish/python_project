import json

with open('iamge_urls.json', 'r') as file:
	img_src = json.load(file);
print(len(img_src))
with open('trial.html', 'w') as file:
	file.write('<html>\n\t<head>\n\t</head>\n\t<body>\n');
	for src in img_src:
		file.write('\n\t\t<img src="' + src + '" >\n\t\t<h2> ' + src + '</h2>');
	file.write('\n\t</body>\n</html>');
