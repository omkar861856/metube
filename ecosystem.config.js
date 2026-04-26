module.exports = {
  apps : [{
    name: 'metube',
    script: 'app/main.py',
    interpreter: 'python3',
    instances: 1,
    autorestart: true,
    watch: false,
    max_memory_restart: '1G',
    env: {
      NODE_ENV: 'production',
      PORT: 8081,
      DOWNLOAD_DIR: './downloads',
      STATE_DIR: './downloads/.metube',
      CUSTOM_DIRS: 'true'
    }
  }]
};
