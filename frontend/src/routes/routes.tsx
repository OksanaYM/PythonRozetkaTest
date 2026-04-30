import {createBrowserRouter} from "react-router";
import {MainLayout} from "../MainLayouts/MainLayout.tsx";
import CategoryPage from "../pages/CategoryPage.tsx";

export const routes = createBrowserRouter([
    {path: '/', element: <MainLayout/>, children:[
            {path: 'category', element: <CategoryPage/>},

        ]}
])