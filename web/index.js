
async function getStatus() {
    document.getElementById('stat_div').appendChild = await eel.send_status();
};

document.getElementById("get_btn").addEventListener('click', function () { getStatus(); })