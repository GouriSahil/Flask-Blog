/** @type {import('tailwindcss').Config} */
export default {
  content: ["./flaskblog/templates/**/*.html"],
  theme: {
    extend: {
      colors: {
        vanilla: {
          DEFAULT: "#F3E5C3",
          muted: "#E8D9B4",
          deep: "#DFC9A0",
        },
        forest: {
          DEFAULT: "#174E4F",
          light: "#1F6567",
          dark: "#0F3839",
        },
      },
      fontFamily: {
        sans: [
          "DM Sans",
          "ui-sans-serif",
          "system-ui",
          "sans-serif",
        ],
      },
      boxShadow: {
        soft: "0 4px 24px -4px rgba(23, 78, 79, 0.12)",
        card: "0 8px 32px -8px rgba(23, 78, 79, 0.14)",
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-out',
        'scale-in': 'scaleIn 0.3s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        scaleIn: {
          '0%': { opacity: '0', transform: 'scale(0.95)' },
          '100%': { opacity: '1', transform: 'scale(1)' },
        },
      },
    },
  },
  plugins: [],
}
