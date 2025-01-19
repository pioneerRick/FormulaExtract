// import { defineConfig } from 'vite';
// import vue from '@vitejs/plugin-vue';
//
// export default defineConfig({
//   plugins: [vue()],
//   server: {
//     proxy: {
//       '/api': {
//         target: 'https://106.14.34.102:14326', // Flask 后端地址
//         changeOrigin: true,
//       },
//     },
//   },
// });

import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/api': {
        target: 'http://106.14.34.102:14325',  // 使用服务器的IP地址
        // target: 'http://192.168.1.103:14326',  // 使用服务器的IP地址
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''), // 可选：去掉 /api 前缀
      },
    },
  },
});
