"use client"

import * as React from "react"
import {
  AudioWaveform,
  BookOpen,
  Bot,
  Command,
  Factory,
  Frame,
  GalleryVerticalEnd,
  HeartPulse,
  LifeBuoy,
  Map,
  NotepadText,
  PieChart,
  Send,
  Settings2,
  SquareTerminal,
} from "lucide-react"

import { NavMain } from "@/components/nav-main"
import { NavProjects } from "@/components/nav-projects"
import { NavUser } from "@/components/nav-user"
import { TeamSwitcher } from "@/components/team-switcher"
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
  SidebarRail,
} from "@/components/ui/sidebar"
import { NavSecondary } from "./nav-secondary"

// This is sample data.
const data = {
  user: {
    name: "Juan Morales",
    email: "juan.exequiel.morales@gmail.com",
    avatar: "/avatars/shadcn.jpg",
  },
  teams: [
    {
      name: "Acme Inc",
      logo: GalleryVerticalEnd,
      plan: "Enterprise",
    },
    {
      name: "Acme Corp.",
      logo: AudioWaveform,
      plan: "Startup",
    },
    {
      name: "Evil Corp.",
      logo: Command,
      plan: "Free",
    },
  ],
  navMain: [
    {
      title: "Resumen",
      url: "#",
      icon: NotepadText,
      isActive: true,
      items: [
        {
          title: "Historial",
          url: "#",
        },
        {
          title: "Estadísticas",
          url: "#",
        },
        {
          title: "Personal",
          url: "#",
        },
      ],
    },
    {
      title: "Accidentes",
      url: "#",
      icon: HeartPulse,
      items: [
        {
          title: "Historial",
          url: "#",
        },
        {
          title: "Estadisticas",
          url: "#",
        },
        {
          title: "Personal",
          url: "#",
        },
      ],
    },
    {
      title: "Capacitaciones",
      url: "#",
      icon: BookOpen,
      items: [
        {
          title: "Iniciar Curso",
          url: "#",
        },
        {
          title: "Crear Curso",
          url: "#",
        },
        {
          title: "Generar Certificado",
          url: "#",
        },
        {
          title: "Historial",
          url: "#",
        },
      ],
    },
    {
      title: "Configuración",
      url: "#",
      icon: Settings2,
      items: [
        {
          title: "Perfil de empresa",
          url: "#",
        },
        {
          title: "Empleados",
          url: "#",
        },
        {
          title: "Roles",
          url: "#",
        },
        {
          title: "Cursos",
          url: "#",
        },
      ],
    },
  ],
  projects: [
    {
      name: "Empresa",
      url: "#",
      icon: Factory,
    },
    {
      name: "Ventas y Marketing",
      url: "#",
      icon: PieChart,
    },
    {
      name: "Complejos",
      url: "#",
      icon: Map,
    },
  ],
  navSecondary: [
    {
      title: "Soporte",
      url: "#",
      icon: LifeBuoy,
    },
    {
      title: "Ayuda",
      url: "#",
      icon: Send,
    },
  ],
}

export function AppSidebar({ ...props }: React.ComponentProps<typeof Sidebar>) {
  return (
    <Sidebar collapsible="icon" {...props}>
      <SidebarHeader>
        <TeamSwitcher teams={data.teams} />
      </SidebarHeader>
      <SidebarContent>
        <NavMain items={data.navMain} />
        <NavProjects projects={data.projects} />
        <NavSecondary items={data.navSecondary} className="mt-auto" />
      </SidebarContent>
      <SidebarFooter>
        <NavUser user={data.user} />
      </SidebarFooter>
      <SidebarRail />
    </Sidebar>
  )
}
