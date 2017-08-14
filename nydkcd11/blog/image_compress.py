from PIL import Image as Img
try:
	import StringIO #python2
except ModuleNotFoundError:
	from io import StringIO #python3

#test save method
def save(self, *args, **kwargs):
	if self.image:
		img = Img.open(StringIO.StringIO(self.image.read()))
		if img.mode != 'RGB':
			img = img.convert('RGB')
		img.thumbnail((self.image.width/1.5,self.image.height/1.5), Img.ANTIALIAS)
		output = StringIO.StringIO()
		img.save(output, format='JPEG', quality=70)
		output.seek(0)
		self.image= InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', output.len, None)
	super(Images, self).save(*args, **kwargs)

