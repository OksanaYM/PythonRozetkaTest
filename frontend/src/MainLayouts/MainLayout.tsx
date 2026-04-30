import {Outlet} from "react-router";
import {Header} from "../Header/Header.tsx";


export const MainLayout = () =>{
    return(
        <>
            <Header/>
            <Outlet/>
        </>
    )
}