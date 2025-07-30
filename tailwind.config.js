/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./web/templates/**/*.html",
    "./web/**/*.py",
  ],
  // ← сюда добавляем
  safelist: [
    'hidden',
    'md:hidden',
  ],

  theme: {
    extend: {
      animation: {
        'fade-in': 'fadeIn 1s ease-in-out forwards',
      },
      keyframes: {
        fadeIn: {
          '0%':   { opacity: 0 },
          '100%': { opacity: 1 },
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
