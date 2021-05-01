x = document.getElementById('copy');

x.addEventListener('click',function(){

		short_url = document.getElementById('short_url');
		short_url.select();
		short_url.setSelectionRange(0, 99999);
		document.execCommand("copy");
		document.getElementById('copied').innerHTML = "URL Copied";

});