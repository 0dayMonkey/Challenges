/*
Quand vous visitez ce lien vous recevez un message.
Renvoyez ce même message à https://www.wechall.net/challenge/training/programming1/index.php?answer=the_message
Votre limite de temps est 1.337 seconds
*/

const https = require('https');
const cookie = "WC=17687231-65384-HwWPH90KLlX1c1pb";

const options = {
  hostname: 'www.wechall.net',
  path: '/challenge/training/programming1/index.php?action=request',
  headers: {
    'Cookie': cookie
  }
};

const req = https.get(options, (res) => {
  let data = '';

  res.on('data', (chunk) => {
    data += chunk;
  });

  res.on('end', () => {
    // Envoyez une autre requête avec le contenu récupéré
    const postOptions = {
      hostname: 'www.wechall.net',
      path: '/challenge/training/programming1/index.php?answer=' + encodeURIComponent(data),
      headers: {
        'Cookie': cookie
      }
    };

    const postReq = https.get(postOptions, (postRes) => {
      let postData = '';

      postRes.on('data', (chunk) => {
        postData += chunk;
      });

      postRes.on('end', () => {
        console.log(postData);
      });
    });

    postReq.on('error', (error) => {
      console.error(error);
    });
  });
});

req.on('error', (error) => {
  console.error(error);
});
