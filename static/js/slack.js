function toggleSection(sectionId) {
    var section = document.getElementById(sectionId);
    if (section.style.display === "none") {
        section.style.display = "block";
    } else {
        section.style.display = "none";
    }
}

function toggleChannels() {
    var channels = document.getElementById("channel-links");
    var dms = document.getElementById("dms");
    var activity = document.getElementById("activity");

    if (channels.style.display === "none") {
        channels.style.display = "block";
        dms.style.display = "none";
        activity.style.display = "none";
    } else {
        channels.style.display = "none";
    }
}

function toggleAddChannelForm() {
    var form = document.getElementById("add-channel-form");
    if (form.style.display === "none") {
        form.style.display = "block";
    } else {
        form.style.display = "none";
    }
}

function addChannel() {
    var channelName = document.querySelector("#add-channel-form input[type='text']").value.trim();
    var visibility = document.querySelector("#add-channel-form input[type='radio']:checked").value;
    if (channelName !== "") {
        var newChannelLink = document.createElement("a");
        newChannelLink.href = "#";
        newChannelLink.textContent = channelName + " (" + visibility + ")";
        var addChannelLink = document.querySelector("#channel-links a:last-of-type");
        var channelLinks = document.getElementById("channel-links");
        channelLinks.insertBefore(newChannelLink, addChannelLink);
        toggleAddChannelForm(); 
    }
}

