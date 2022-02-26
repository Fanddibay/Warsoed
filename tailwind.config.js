const { colors } = require("tailwindcss/defaultTheme");

module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    spacing: {
      px: "1px",
      0: "0px",
      0.5: "none",
      1: "0.25rem",
      1.5: "0.375rem",
      2: "0.5rem",
      2.5: "0.625rem",
      3: "0.75rem",
      3.5: "0.875rem",
      4: "1rem",
      5: "1.25rem",
      6: "1.5rem",
      7: "1.75rem",
      8: "2rem",
      9: "2.25rem",
      10: "2.5rem",
      11: "2.75rem",
      12: "3rem",
      14: "3.5rem",
      16: "4rem",
      18: "4.5rem",
      20: "5rem",
      24: "6rem",
      28: "7rem",
      30: "70px",
      32: "8rem",
      34: "8.5rem",
      36: "9rem",
      40: "10rem",
      44: "11rem",
      48: "12rem",
      52: "13rem",
      56: "18rem",
      60: "15rem",
      64: "50vh",
      72: "18rem",
      80: "20rem",
      88: "22rem",
      96: "24rem",
    },
    fontFamily: {
      sans: ['"poppins'],
    },

    letterSpacing: {
      tightest: "-.075em",
      tighter: "-.05em",
      tight: "-.025em",
      normal: "0",
      wide: "2px",
      wider: ".05em",
      widest: ".1em",
      widest: ".25em",
    },
    extend: {
      backgroundImage: (theme) => ({
        "hero-img": "url('/src/images/jumbotron.png')",
      }),
      colors: {
        yellow: {
          ...colors.yellow,
          400: "#fd7014",
        },
        gray: {
          ...colors.gray,
          400: "#DCD6F7",
          ...colors.gray,
          500: "#B1B1B1",
          ...colors.gray,
          900: "#2e2e2e",
        },
        blue: {
          ...colors.blue,
          400: "#2D295C",
        },
        red: {
          ...colors.red,
          500: "#F54748",
        },
      },
    },
  },
  plugins: [],
};
