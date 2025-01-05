const fileInput = document.getElementById('fileInput');
const processBtn = document.getElementById('processBtn');
const downloadBtn = document.getElementById('downloadBtn');

fileInput.addEventListener('change', () => {
    if(fileInput.files.length === 0){
        processBtn.disabled = true
        downloadBtn.disabled = true 

        processBtn.style.backgroundColor = 'grey'
        downloadBtn.style.backgroundColor = 'grey'
    }
    else{
        processBtn.disabled = false
        downloadBtn.disabled = false    

        processBtn.style.backgroundColor = '#007bff'
        downloadBtn.style.backgroundColor = '#28a745'
    }
})


console.log('Hello, World!');
