module.exports = {
  content: ["../templates/*.{html,js}", "../templates/**/*.{html,js}"],
  theme: {
    extend: {
      backgroundImage: {
        "header-image": "url('/static/img/home-bg.jpg')",
      },
    },
  },
  plugins: [require("@tailwindcss/typography"), require("daisyui")],
  daisyui: {
    themes: ["cupcake"],
  },
};
