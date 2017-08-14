from PIL import Image as Img
try:
	from io import StringIO #python3
	from io import BytesIO
except ModuleNotFoundError:
	import StringIO #python2
	import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
#test save method
def save(self, *args, **kwargs):
	if self.image:
		img = Img.open(StringIO(str(self.image.read())))
		if img.mode != 'RGB':
			img = img.convert('RGB')
		img.thumbnail((self.image.width/1.5,self.image.height/1.5), Img.ANTIALIAS)
		output = StringIO()
		img.save(output, format='JPEG', quality=70)
		output.seek(0)
		self.image= InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', output.len, None)
	super(Image, self).save(*args, **kwargs)

'''
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
	super(Image, self).save(*args, **kwargs)
'''
def compress(image):
	if image:
		img= Img.open(BytesIO(image.read()))
		if img.mode != 'RGB':
			img = img.convert('RGB')
		#img.thumbnail((image.width/1.5,image.height/1.5), Img.ANTIALIAS)
		output=BytesIO()
		img.save(output, format='JPEG', quality=70)
		output.seek(0)
		try:
			image= InMemoryUploadedFile(output,'ImageField', "%s.jpg" %image.name.split('.')[0], 'image/jpeg', output.getbuffer().nbytes, None)
		except AttributeError:
			image= InMemoryUploadedFile(output,'ImageField', "%s.jpg" %image.name.split('.')[0], 'image/jpeg', len(output.getvalue()), None)
	return image

