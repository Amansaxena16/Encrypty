const fileInput = document.getElementById('fileInput');
const processBtn = document.getElementById('processBtn');
const downloadBtn = document.getElementById('downloadBtn');

processBtn.addEventListener('click', (e) => {
    if(fileInput.files.length == 0){
        alert('Please select a file before submitting!');
        e.preventDefault()
        return;        
    }

    setTimeout(() =>{
        processBtn.disabled = true; // Disable the button after a single click
        processBtn.innerHTML = "Processing...." // Showing the loading state of the button
    },100) // / Small delay (100ms) to allow the request to be sent

    setTimeout(() => {
        window.location.reload()
    }, 1000); // Reload after 1 Seconds
})

fileInput.addEventListener('change', () => {
    processBtn.disabled = false
    downloadBtn.disabled = false
})
