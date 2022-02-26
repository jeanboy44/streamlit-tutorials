# Core Pkg
import streamlit as st

# Components
# import streamlit.components.v1 as components
import streamlit.components.v1 as stc
import codecs


def render_html(file, height=700, width=700):
	html_file = codecs.open(file, "r")
	page = html_file.read()
	stc.html(page, width=width, height=height, scrolling=True)


def main():
	col1, col2 = st.columns(2)
	with col1:
		st.title("Streamlit Static Components Tut")
		with st.expander("Components Explanation"):
			st.image("data/streamlit_component_types_jcharistech.png")
		stc.html("<p style='color:red;'>Streamlit is Awesome </p>", height=100)
		st.markdown(
				"<p style='color:blue;'>Streamlit is Awesome </p>", unsafe_allow_html=True
		)

		st.text("From W3Schools")
		stc.html("""
			<style>
	* {box-sizing: border-box}
	body {font-family: Verdana, sans-serif; margin:0}
	.mySlides {display: none}
	img {vertical-align: middle;}

	/* Slideshow container */
	.slideshow-container {
	max-width: 1000px;
	position: relative;
	margin: auto;
	}

	/* Next & previous buttons */
	.prev, .next {
	cursor: pointer;
	position: absolute;
	top: 50%;
	width: auto;
	padding: 16px;
	margin-top: -22px;
	color: white;
	font-weight: bold;
	font-size: 18px;
	transition: 0.6s ease;
	border-radius: 0 3px 3px 0;
	user-select: none;
	}

	/* Position the "next button" to the right */
	.next {
	right: 0;
	border-radius: 3px 0 0 3px;
	}

	/* On hover, add a black background color with a little bit see-through */
	.prev:hover, .next:hover {
	background-color: rgba(0,0,0,0.8);
	}

	/* Caption text */
	.text {
	color: #f2f2f2;
	font-size: 15px;
	padding: 8px 12px;
	position: absolute;
	bottom: 8px;
	width: 100%;
	text-align: center;
	}

	/* Number text (1/3 etc) */
	.numbertext {
	color: #f2f2f2;
	font-size: 12px;
	padding: 8px 12px;
	position: absolute;
	top: 0;
	}

	/* The dots/bullets/indicators */
	.dot {
	cursor: pointer;
	height: 15px;
	width: 15px;
	margin: 0 2px;
	background-color: #bbb;
	border-radius: 50%;
	display: inline-block;
	transition: background-color 0.6s ease;
	}

	.active, .dot:hover {
	background-color: #717171;
	}

	/* Fading animation */
	.fade {
	-webkit-animation-name: fade;
	-webkit-animation-duration: 1.5s;
	animation-name: fade;
	animation-duration: 1.5s;
	}

	@-webkit-keyframes fade {
	from {opacity: .4} 
	to {opacity: 1}
	}

	@keyframes fade {
	from {opacity: .4} 
	to {opacity: 1}
	}

	/* On smaller screens, decrease text size */
	@media only screen and (max-width: 300px) {
	.prev, .next,.text {font-size: 11px}
	}
	</style>
	<body>

	<div class="slideshow-container">

	<div class="mySlides fade">
	<div class="numbertext">1 / 3</div>
	<img src="https://www.w3schools.com/howto/img_nature_wide.jpg" style="width:100%">
	<div class="text">Caption Text</div>
	</div>

	<div class="mySlides fade">
	<div class="numbertext">2 / 3</div>
	<img src="https://www.w3schools.com/howto/img_snow_wide.jpg" style="width:100%">
	<div class="text">Caption Two</div>
	</div>

	<div class="mySlides fade">
	<div class="numbertext">3 / 3</div>
	<img src="https://www.w3schools.com/howto/img_mountains_wide.jpg" style="width:100%">
	<div class="text">Caption Three</div>
	</div>

	<a class="prev" onclick="plusSlides(-1)">&#10094;</a>
	<a class="next" onclick="plusSlides(1)">&#10095;</a>

	</div>
	<br>

	<div style="text-align:center">
	<span class="dot" onclick="currentSlide(1)"></span> 
	<span class="dot" onclick="currentSlide(2)"></span> 
	<span class="dot" onclick="currentSlide(3)"></span> 
	</div>

	<script>
	var slideIndex = 1;
	showSlides(slideIndex);

	function plusSlides(n) {
	showSlides(slideIndex += n);
	}

	function currentSlide(n) {
	showSlides(slideIndex = n);
	}

	function showSlides(n) {
	var i;
	var slides = document.getElementsByClassName("mySlides");
	var dots = document.getElementsByClassName("dot");
	if (n > slides.length) {slideIndex = 1}    
	if (n < 1) {slideIndex = slides.length}
	for (i = 0; i < slides.length; i++) {
		slides[i].style.display = "none";  
	}
	for (i = 0; i < dots.length; i++) {
		dots[i].className = dots[i].className.replace(" active", "");
	}
	slides[slideIndex-1].style.display = "block";  
	dots[slideIndex-1].className += " active";
	}
	</script>

	</body>

	"""
		)

		# Working with IFrame
		st.text("Streamlit Webpage")
		stc.iframe("https://streamlit.io", height=1000, scrolling=True)
	with col2:
		code = """st.title("Streamlit Static Components Tut")
with st.expander("Components Explanation"):
	st.image("data/streamlit_component_types_jcharistech.png")
stc.html("<p style='color:red;'>Streamlit is Awesome </p>", height=100)
st.markdown("<p style='color:blue;'>Streamlit is Awesome </p>", unsafe_allow_html=True)
st.text("From W3Schools")
stc.html(\"\"\"
		<style>
* {box-sizing: border-box}
body {font-family: Verdana, sans-serif; margin:0}
.mySlides {display: none}
img {vertical-align: middle;}

/* Slideshow container */
.slideshow-container {
max-width: 1000px;
position: relative;
margin: auto;
}

/* Next & previous buttons */
.prev, .next {
cursor: pointer;
position: absolute;
top: 50%;
width: auto;
padding: 16px;
margin-top: -22px;
color: white;
font-weight: bold;
font-size: 18px;
transition: 0.6s ease;
border-radius: 0 3px 3px 0;
user-select: none;
}

/* Position the "next button" to the right */
.next {
right: 0;
border-radius: 3px 0 0 3px;
}

/* On hover, add a black background color with a little bit see-through */
.prev:hover, .next:hover {
background-color: rgba(0,0,0,0.8);
}

/* Caption text */
.text {
color: #f2f2f2;
font-size: 15px;
padding: 8px 12px;
position: absolute;
bottom: 8px;
width: 100%;
text-align: center;
}

/* Number text (1/3 etc) */
.numbertext {
color: #f2f2f2;
font-size: 12px;
padding: 8px 12px;
position: absolute;
top: 0;
}

/* The dots/bullets/indicators */
.dot {
cursor: pointer;
height: 15px;
width: 15px;
margin: 0 2px;
background-color: #bbb;
border-radius: 50%;
display: inline-block;
transition: background-color 0.6s ease;
}

.active, .dot:hover {
background-color: #717171;
}

/* Fading animation */
.fade {
-webkit-animation-name: fade;
-webkit-animation-duration: 1.5s;
animation-name: fade;
animation-duration: 1.5s;
}

@-webkit-keyframes fade {
from {opacity: .4} 
to {opacity: 1}
}

@keyframes fade {
from {opacity: .4} 
to {opacity: 1}
}

/* On smaller screens, decrease text size */
@media only screen and (max-width: 300px) {
.prev, .next,.text {font-size: 11px}
}
</style>
<body>

<div class="slideshow-container">

<div class="mySlides fade">
<div class="numbertext">1 / 3</div>
<img src="https://www.w3schools.com/howto/img_nature_wide.jpg" style="width:100%">
<div class="text">Caption Text</div>
</div>

<div class="mySlides fade">
<div class="numbertext">2 / 3</div>
<img src="https://www.w3schools.com/howto/img_snow_wide.jpg" style="width:100%">
<div class="text">Caption Two</div>
</div>

<div class="mySlides fade">
<div class="numbertext">3 / 3</div>
<img src="https://www.w3schools.com/howto/img_mountains_wide.jpg" style="width:100%">
<div class="text">Caption Three</div>
</div>

<a class="prev" onclick="plusSlides(-1)">&#10094;</a>
<a class="next" onclick="plusSlides(1)">&#10095;</a>

</div>
<br>

<div style="text-align:center">
<span class="dot" onclick="currentSlide(1)"></span> 
<span class="dot" onclick="currentSlide(2)"></span> 
<span class="dot" onclick="currentSlide(3)"></span> 
</div>

<script>
var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
showSlides(slideIndex += n);
}

function currentSlide(n) {
showSlides(slideIndex = n);
}

function showSlides(n) {
var i;
var slides = document.getElementsByClassName("mySlides");
var dots = document.getElementsByClassName("dot");
if (n > slides.length) {slideIndex = 1}    
if (n < 1) {slideIndex = slides.length}
for (i = 0; i < slides.length; i++) {
	slides[i].style.display = "none";  
}
for (i = 0; i < dots.length; i++) {
	dots[i].className = dots[i].className.replace(" active", "");
}
slides[slideIndex-1].style.display = "block";  
dots[slideIndex-1].className += " active";
}
</script>

</body>
\"\"\")

# Working with IFrame
st.text("Streamlit Webpage")
stc.iframe("https://streamlit.io", height=1000, scrolling=True)
		"""
		st.title("Code")
		st.code(code)
if __name__ == "__main__":
		main()
