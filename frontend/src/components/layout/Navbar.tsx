import { useState } from "react";
import { Link, useLocation } from "react-router-dom";
import { motion, AnimatePresence } from "framer-motion";
import { Brain, Menu, X } from "lucide-react";

const navItems = [
  { label: "Home", path: "/" },
  { label: "Analyze", path: "/analyze" },
  { label: "Contact", path: "/contact" },
];

export default function Navbar() {
  const [open, setOpen] = useState(false);
  const { pathname } = useLocation();

  return (
    <nav className="fixed top-0 inset-x-0 z-50 glass-strong">
      <div className="container mx-auto flex h-16 items-center justify-between px-6">
        <Link to="/" className="flex items-center gap-2 group">
          <Brain className="h-7 w-7 text-primary transition-transform duration-300 group-hover:scale-110" />
          <span className="text-lg font-bold tracking-tight">
            <span className="gradient-text">XAI</span> Lite
          </span>
        </Link>

        {/* Desktop */}
        <div className="hidden md:flex items-center gap-1">
          {navItems.map((item) => (
            <Link
              key={item.path}
              to={item.path}
              className={`relative px-4 py-2 text-sm font-medium rounded-lg transition-colors duration-200 ${
                pathname === item.path
                  ? "text-primary-foreground"
                  : "text-muted-foreground hover:text-foreground"
              }`}
            >
              {pathname === item.path && (
                <motion.div
                  layoutId="nav-pill"
                  className="absolute inset-0 rounded-lg bg-primary/20"
                  transition={{ type: "spring", stiffness: 400, damping: 30 }}
                />
              )}
              <span className="relative z-10">{item.label}</span>
            </Link>
          ))}
        </div>

        {/* Mobile toggle */}
        <button
          onClick={() => setOpen(!open)}
          className="md:hidden p-2 rounded-lg text-muted-foreground hover:text-foreground transition-colors"
          aria-label="Toggle menu"
        >
          {open ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
        </button>
      </div>

      {/* Mobile menu */}
      <AnimatePresence>
        {open && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: "auto" }}
            exit={{ opacity: 0, height: 0 }}
            className="md:hidden glass-strong overflow-hidden"
          >
            <div className="px-6 py-4 flex flex-col gap-2">
              {navItems.map((item) => (
                <Link
                  key={item.path}
                  to={item.path}
                  onClick={() => setOpen(false)}
                  className={`px-4 py-3 rounded-lg text-sm font-medium transition-colors ${
                    pathname === item.path
                      ? "bg-primary/20 text-foreground"
                      : "text-muted-foreground hover:text-foreground hover:bg-primary/10"
                  }`}
                >
                  {item.label}
                </Link>
              ))}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </nav>
  );
}
