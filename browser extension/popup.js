const app_id = '3tjqahi5';

let channel_name;
let video_id;

let get_value = async (key) => {
    const response = await fetch(`https://keyvalue.immanuel.co/api/KeyVal/GetValue/${app_id}/${key}`, {});
    return await response.json();
}

let set_value = async (key, value) => {
    const request = await fetch(`https://keyvalue.immanuel.co/api/KeyVal/UpdateValue/${app_id}/${key}/${value}`, { method: 'POST' });
}

window.addEventListener('load', function () {
    window.setInterval(myCallback, 5000);

    setTimeout(async function () {
        channel_name = document.getElementsByClassName('yt-simple-endpoint style-scope yt-formatted-string')[0].innerText;
        video_id = window.location.href.split('watch?v=')[1];

        console.log(channel_name);

        let allcreators = await get_value('allcreators');
        console.log("allcreators", allcreators);
        if (!allcreators.includes(channel_name)) {
            await set_value('allcreators', allcreators + "," + channel_name);
        }

        let allids = await get_value(channel_name);
        console.log("allids", allids);
        if (!allids.includes(video_id)) {
            await set_value(channel_name, allids + ',' + video_id);
        }
    }, 5000);

})

async function myCallback() {
    let current_time = document.getElementsByClassName('video-stream')[0].currentTime;
    console.log(current_time);

    let max_time = await get_value(video_id);
    if (max_time === '' || max_time < current_time) {
        await set_value(video_id, Math.floor(current_time));
    }
}