import App from "./SidebarCostum";

export default {
  title: "Components/Sidebar",
  component: App,
  //   decorators: [withNextRouter()],
  tags: ["autodocs"],
  argTypes: {},
};

export const Sidebar = {
  parameters: {
    nextjs: {
      appDirectory: true,
      navigation: {
        pathname: "update/[id]",
        asPath: "/update/499",
        query: {
          id: 499,
        },
      },
    },
  },
};
