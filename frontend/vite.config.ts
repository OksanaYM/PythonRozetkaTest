
import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig(({ mode }) => {
  // Завантажуємо змінні з .env файлу
  const env = loadEnv(mode, process.cwd(), '');

  return {
    plugins: [react()],
    build: {
      // Якщо в .env є BUILD_PATH, використовуємо його, інакше — 'dist'
      outDir: env.BUILD_PATH || 'dist',
      emptyOutDir: true,
    },
  }
})
