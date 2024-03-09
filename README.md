[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Penjelasan Singkat Algoritma Greedy yang Diimplementasikan 💎
Diamonds adalah permainan papan dimana para pemainnya mengambil diamond sebanyak-banyaknya dalam rentang waktu yang ditentukan.
Di dalamnya terdapat pemain, teleporter, base, dan tombol reset diamond.
Pada algoritma dalam bot ini, bot akan mencari diamond terdekat dengan memanfaatkan teleporter dan tombol reset diamond. Diamonds yang telah terkumpul juga akan dikumpulkan ke base pemain sebelum waktu habis agar terhitung sebagai poin sang pemain.

# Menginstall Requirements dan Menjalankan Program 🔨
Clone
1. Install Requirements
    - Install Node.js pada https://nodejs.org/en
    - Install docker desktop https://www.docker.com/products/docker-desktop/
    - Install Yarn
    Eksekusi command line berikut untuk menginstall Yarn
    '''
    npm install --global yarn
    '''
2. Menyiapkan board permainan
    Buka folder game
    '''
    cd src/game
    '''
    Install dependencies
    '''
    yarn
    '''
    Setup default environment variable (untuk windows)
    '''
    .\scripts\copy-env.bat
    '''
    Setup default environment variable (untuk linux)
    '''
    chmod +x ./scripts/copy-env.sh
./scripts/copy-env.sh
    '''
    Setup local database (untuk windows)
    '''
    docker compose up -d database
    ./scripts/setup-db-prisma.bat
    '''
    Setup local database (untuk linux)
    '''
    docker compose up -d database
    chmod +x ./scripts/setup-db-prisma.sh
./scripts/setup-db-prisma.sh
    '''
    Build
    '''
    npm run build
    '''
    Run
    '''
    npm run start
    '''
    Jika semua step sudah pernah dilakukan untuk menjalankan kembali server hanya perlu untuk melakukan run
    '''
    npm run start
    '''
3. Menjalankan bot
    Install python https://www.python.org/downloads/
    Buka folder bot
    '''
    cd src/bot
    '''
    (jika dari folder repository)
    install requiremnts bot
    '''
    pip install -r requirements.txt
    '''
    Run
    - menjalankan 1 bot
    '''
    python main.py --logic "chosen_logic" --email=your_email@example.com --name=your_name --password=your_password --team etimo
    '''
    contoh:
    '''
    python main.py --logic Damai --email=your_email@example.com --name=your_name --password=your_password --team etimo
    '''
    - Menjalankan bot sesuai dengan run-bots
    Windows
    '''
    ./run-bots.bat
    '''
    Linux
    '''
    ./run-bots.bat
    '''
# Author 💻
- Muhammad Fuad Nugraha - 10023520
- Emery Fathan Zwageri - 13522079
- Rayendra Althaf Taraka Noor - 13522107

©️ All rights and credits reserved to [Etimo](https://github.com/Etimo)
