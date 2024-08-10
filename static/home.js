document.addEventListener('DOMContentLoaded', function() {
    const text = "Hello, Welcome To RayBlogs"; 
    let index = 0; 
    
    function type() {
        if (index < text.length) {
            document.getElementById("typed-text").innerHTML += text.charAt(index);
            index++;
            setTimeout(type, 150); 
        }
    }
    
    
    document.getElementById("typed-text").innerHTML = '';
    type(); 
});
