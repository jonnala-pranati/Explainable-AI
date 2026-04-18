import { useState } from "react";
import { motion } from "framer-motion";
import { Mail, MapPin, Send, Sparkles } from "lucide-react";
import Navbar from "@/components/layout/Navbar";
import Footer from "@/components/layout/Footer";
import { toast } from "sonner";

export default function Contact() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    subject: "",
    message: "",
  });
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [isSubmitting, setIsSubmitting] = useState(false);

  const validateForm = () => {
    const newErrors: Record<string, string> = {};

    if (!formData.name.trim()) {
      newErrors.name = "Name is required";
    }

    if (!formData.email.trim()) {
      newErrors.email = "Email is required";
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
      newErrors.email = "Please enter a valid email address";
    }

    if (!formData.subject.trim()) {
      newErrors.subject = "Subject is required";
    }

    if (!formData.message.trim()) {
      newErrors.message = "Message is required";
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (validateForm()) {
      setIsSubmitting(true);

      // Simulate API call
      setTimeout(() => {
        setIsSubmitting(false);
        toast.success("Message sent successfully!");
        setFormData({ name: "", email: "", subject: "", message: "" });
      }, 1500);
    }
  };

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
    // Clear error when user starts typing
    if (errors[name]) {
      setErrors((prev) => ({ ...prev, [name]: "" }));
    }
  };

  return (
    <div className="min-h-screen bg-background relative overflow-hidden">
      {/* Background gradient effects */}
      <div className="fixed inset-0 pointer-events-none">
        <div className="absolute top-0 left-1/4 w-96 h-96 bg-primary/10 rounded-full blur-3xl" />
        <div className="absolute bottom-0 right-1/4 w-96 h-96 bg-blue-500/10 rounded-full blur-3xl" />
      </div>

      <Navbar />

      <main className="relative pt-24 pb-16 px-6">
        <div className="container mx-auto max-w-6xl">
          {/* Hero Section */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="text-center mb-16"
          >
            <motion.div
              initial={{ scale: 0 }}
              animate={{ scale: 1 }}
              transition={{ delay: 0.2, type: "spring", stiffness: 200 }}
              className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary/10 border border-primary/20 mb-6"
            >
              <Sparkles className="h-4 w-4 text-primary" />
              <span className="text-sm font-medium text-primary">Get in Touch</span>
            </motion.div>
            <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold mb-4">
              <span className="gradient-text">Contact Us</span>
            </h1>
            <p className="text-lg md:text-xl text-muted-foreground max-w-2xl mx-auto">
              Have questions about AI predictions or explanations? We'd love to hear from you.
            </p>
          </motion.div>

          {/* Main Section */}
          <div className="grid lg:grid-cols-2 gap-8">
            {/* Contact Form */}
            <motion.div
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: 0.3, duration: 0.6 }}
            >
              <div className="glass-strong rounded-2xl p-8 hover:glow-sm transition-all duration-500">
                <form onSubmit={handleSubmit} className="space-y-6">
                  {/* Name */}
                  <div>
                    <label htmlFor="name" className="block text-sm font-medium mb-2">
                      Name <span className="text-destructive">*</span>
                    </label>
                    <input
                      type="text"
                      id="name"
                      name="name"
                      value={formData.name}
                      onChange={handleChange}
                      placeholder="Your name"
                      className={`w-full px-4 py-3 rounded-lg bg-background/50 border ${
                        errors.name ? "border-destructive" : "border-border"
                      } focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-all duration-200`}
                    />
                    {errors.name && (
                      <p className="text-destructive text-sm mt-1">{errors.name}</p>
                    )}
                  </div>

                  {/* Email */}
                  <div>
                    <label htmlFor="email" className="block text-sm font-medium mb-2">
                      Email <span className="text-destructive">*</span>
                    </label>
                    <input
                      type="email"
                      id="email"
                      name="email"
                      value={formData.email}
                      onChange={handleChange}
                      placeholder="your@email.com"
                      className={`w-full px-4 py-3 rounded-lg bg-background/50 border ${
                        errors.email ? "border-destructive" : "border-border"
                      } focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-all duration-200`}
                    />
                    {errors.email && (
                      <p className="text-destructive text-sm mt-1">{errors.email}</p>
                    )}
                  </div>

                  {/* Subject */}
                  <div>
                    <label htmlFor="subject" className="block text-sm font-medium mb-2">
                      Subject <span className="text-destructive">*</span>
                    </label>
                    <input
                      type="text"
                      id="subject"
                      name="subject"
                      value={formData.subject}
                      onChange={handleChange}
                      placeholder="What's this about?"
                      className={`w-full px-4 py-3 rounded-lg bg-background/50 border ${
                        errors.subject ? "border-destructive" : "border-border"
                      } focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-all duration-200`}
                    />
                    {errors.subject && (
                      <p className="text-destructive text-sm mt-1">{errors.subject}</p>
                    )}
                  </div>

                  {/* Message */}
                  <div>
                    <label htmlFor="message" className="block text-sm font-medium mb-2">
                      Message <span className="text-destructive">*</span>
                    </label>
                    <textarea
                      id="message"
                      name="message"
                      value={formData.message}
                      onChange={handleChange}
                      placeholder="Your message..."
                      rows={5}
                      className={`w-full px-4 py-3 rounded-lg bg-background/50 border ${
                        errors.message ? "border-destructive" : "border-border"
                      } focus:border-primary focus:ring-2 focus:ring-primary/20 outline-none transition-all duration-200 resize-none`}
                    />
                    {errors.message && (
                      <p className="text-destructive text-sm mt-1">{errors.message}</p>
                    )}
                  </div>

                  {/* Submit Button */}
                  <motion.button
                    type="submit"
                    disabled={isSubmitting}
                    whileHover={{ scale: 1.02 }}
                    whileTap={{ scale: 0.98 }}
                    className="w-full py-4 rounded-lg bg-gradient-to-r from-primary to-blue-500 text-white font-semibold flex items-center justify-center gap-2 hover:shadow-lg hover:shadow-primary/25 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    {isSubmitting ? (
                      <>
                        <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                        Sending...
                      </>
                    ) : (
                      <>
                        <Send className="h-5 w-5" />
                        Send Message
                      </>
                    )}
                  </motion.button>
                </form>
              </div>
            </motion.div>

            {/* Contact Info Panel */}
            <motion.div
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: 0.4, duration: 0.6 }}
              className="space-y-6"
            >
              {/* Email Card */}
              <div className="glass-strong rounded-2xl p-6 hover:glow-sm transition-all duration-500 hover:translate-y-[-4px]">
                <div className="flex items-start gap-4">
                  <div className="p-3 rounded-lg bg-primary/10">
                    <Mail className="h-6 w-6 text-primary" />
                  </div>
                  <div>
                    <h3 className="font-semibold mb-1">Email</h3>
                    <a
                      href="mailto:hello@ai-lite.com"
                      className="text-muted-foreground hover:text-primary transition-colors"
                    >
                      hello@ai-lite.com
                    </a>
                  </div>
                </div>
              </div>

              {/* Location Card */}
              <div className="glass-strong rounded-2xl p-6 hover:glow-sm transition-all duration-500 hover:translate-y-[-4px]">
                <div className="flex items-start gap-4">
                  <div className="p-3 rounded-lg bg-primary/10">
                    <MapPin className="h-6 w-6 text-primary" />
                  </div>
                  <div>
                    <h3 className="font-semibold mb-1">Location</h3>
                    <p className="text-muted-foreground">India</p>
                  </div>
                </div>
              </div>

              {/* Project Owner Card */}
              <div className="glass-strong rounded-2xl p-6 hover:glow-sm transition-all duration-500 hover:translate-y-[-4px]">
                <div className="flex items-center gap-4">
                  <div className="w-12 h-12 rounded-full bg-gradient-to-br from-primary to-blue-500 flex items-center justify-center">
                    <span className="text-white font-bold text-lg">P</span>
                  </div>
                  <div>
                    <h3 className="font-semibold">Pranati</h3>
                    <p className="text-sm text-muted-foreground">Project Owner</p>
                  </div>
                </div>
              </div>
            </motion.div>
          </div>
        </div>
      </main>

      <Footer />
    </div>
  );
}
