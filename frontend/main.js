document.getElementById('probForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const fd = new FormData(e.target);

  const body = {
    title: fd.get('title'),
    type: fd.get('type'),
    query_text: fd.get('query_text')
  };

  console.log(body);

});