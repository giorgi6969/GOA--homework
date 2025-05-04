const grid = document.getElementById('grid');
const areas = [
  { name: 'hero', text: '1' },
  { name: 'aside1', text: '3' },
  { name: 'aside2', text: '4' },
  { name: 'banner', text: '2' },
  { name: 'box5', text: '5' },
  { name: 'box6', text: '6' },
  { name: 'box7', text: '7' },
  { name: 'box8', text: '8' },
  { name: 'box9', text: '9' }
];

areas.forEach(area => {
  const div = document.createElement('div');
  div.classList.add('item', area.name);
  div.textContent = area.text;
  grid.appendChild(div);
});
