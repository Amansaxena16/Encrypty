const fileInput = document.getElementById('fileInput');
const processBtn = document.getElementById('processBtn');
const downloadBtn = document.getElementById('downloadBtn');

processBtn.addEventListener('click', () => {
    if(fileInput.files.length == 0){
        processBtn.disabled = true;
        downloadBtn.disabled = true 
        alert('Please select a file before submitting!');
    }
})

fileInput.addEventListener('change', () => {
    processBtn.disabled = false
    downloadBtn.disabled = false
})

