import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/api': {
        target: 'http://106.14.34.102:14325',  // 使用服务器的IP地址(后端通过宝塔部署之后可以这样用)
        // target: 'http:127.0.0.1:14325',  // 使用服务器的IP地址
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''), // 可选：去掉 /api 前缀
      },
    },
  },
});
