/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./web/templates/**/*.html",
    "./web/**/*.py",
  ],

  safelist: [
    'hidden',
    'md:hidden',
    'max-h-0',
    'max-h-96',
    'opacity-0',
    'opacity-100',
    'pointer-events-none',
    'pointer-events-auto',
    'rotate-45',
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
