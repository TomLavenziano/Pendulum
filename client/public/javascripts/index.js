const note = {
    note: "Have a terrible time snowboarding next thursday"
};

const encodedNote = encodeURI("Have a terrible time snowboarding next thursday")

console.log(JSON.stringify(note))
console.log(encodedNote);

fetch('http://localhost:8000/SmartNote?note=' + encodedNote, {
        method: "GET",
        mode: "no-cors",
        // body: JSON.stringify(note),
        // body: '{"note": "TEST"}',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
    })
    .then(res => {
        console.log(res);
        let noteHolder = document.getElementsByClassName('noteHolder')
        noteHolder.innerHTML = JSON.stringify(res)
    });
