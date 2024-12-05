document.addEventListener('DOMContentLoaded', function() {
    const laundryStatusDiv = document.getElementById('laundry-status');
    const floors = 10;
    const machinesPerFloor = 2;

    function createWashingMachine(id) {
        const machineDiv = document.createElement('div');
        machineDiv.classList.add('washing-machine');
        machineDiv.id = `machine-${id}`;

        const statusDiv = document.createElement('div');
        statusDiv.classList.add('status', 'available');
        statusDiv.textContent = '空閒';

        machineDiv.appendChild(statusDiv);
        return machineDiv;
    }

    function createFloor(floorNumber) {
        const floorDiv = document.createElement('div');
        floorDiv.classList.add('floor');

        const floorTitle = document.createElement('h2');
        floorTitle.textContent = `第 ${floorNumber} 樓`;
        floorDiv.appendChild(floorTitle);

        for (let i = 1; i <= machinesPerFloor; i++) {
            const machineId = `${floorNumber}-${i}`;
            floorDiv.appendChild(createWashingMachine(machineId));
        }

        return floorDiv;
    }

    for (let i = 1; i <= floors; i++) {
        laundryStatusDiv.appendChild(createFloor(i));
    }

    function toggleStatus(machineId) {
        const machineDiv = document.getElementById(`machine-${machineId}`);
        const statusDiv = machineDiv.querySelector('.status');

        if (statusDiv.classList.contains('available')) {
            statusDiv.classList.remove('available');
            statusDiv.classList.add('in-use');
            statusDiv.textContent = '使用中';
        } else {
            statusDiv.classList.remove('in-use');
            statusDiv.classList.add('available');
            statusDiv.textContent = '空閒';
        }
    }

    // 模擬洗衣機狀態切換，每5秒隨機切換一台洗衣機
    setInterval(function() {
        const randomFloor = Math.floor(Math.random() * floors) + 1;
        const randomMachine = Math.floor(Math.random() * machinesPerFloor) + 1;
        const machineId = `${randomFloor}-${randomMachine}`;
        toggleStatus(machineId);
    }, 5000);
});
