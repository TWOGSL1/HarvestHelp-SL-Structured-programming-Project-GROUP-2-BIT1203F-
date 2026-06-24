import tkinter as tk
from tkinter import ttk, messagebox
import csv
from pathlib import Path

# Constants
PAPER = "#FDFDFD"
MUTED = "#6C757D"
INK = "#212529"
MINT = "#F0FFF4"
PRIMARY = "#2D3748"
RED = "#E53E3E"
LINE = "#E2E8F0"
EXPORT_FILE = Path("harvest_records.csv")

CROP_DATA = {
    "Rice": {
        "yield_per_acre": 1200,
        "seed_kg": 50,
        "season": "Rainy Season (May-Oct)",
        "water_need": "High",
        "advice": "Ensure proper drainage and timely weeding."
    },
    "Cassava": {
        "yield_per_acre": 5000,
        "seed_kg": 200,
        "season": "Year-round",
        "water_need": "Moderate",
        "advice": "Use high-yielding varieties and maintain soil fertility."
    },
    "Maize": {
        "yield_per_acre": 1500,
        "seed_kg": 25,
        "season": "Early Rainy Season",
        "water_need": "Moderate",
        "advice": "Monitor for pests like fall armyworm."
    }
}

DEMO_VALUES = {
    "Farmer name": "Moses Mansaray",
    "Crop": "Rice",
    "District": "Freetown",
    "Risk level": "Low",
    "Land size (acres)": "2.5",
    "Seed cost (SLE)": "1500",
    "Fertilizer cost (SLE)": "2000",
    "Labor cost (SLE)": "3000",
    "Expected price per kg": "15"
}


# Helper Functions
def safe_float(value, field_name):
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"Invalid input for {field_name}. Please enter a number.")


def format_currency(amount):
    return f"SLE {amount:,.2f}"


def calculate_projection(crop, district, acres, seed_cost, fertilizer_cost, labor_cost, price, risk):
    data = CROP_DATA.get(crop, {"yield_per_acre": 1000})
    expected_yield = acres * data["yield_per_acre"]
    revenue = expected_yield * price
    total_cost = seed_cost + fertilizer_cost + labor_cost
    profit = revenue - total_cost

    if profit > 10000:
        status = "Highly Profitable"
        status_color = "#38A169"  # Green
    elif profit > 0:
        status = "Profitable"
        status_color = "#3182CE"  # Blue
    else:
        status = "Risk of Loss"
        status_color = "#E53E3E"  # Red

    return {
        "expected_yield": expected_yield,
        "revenue": revenue,
        "total_cost": total_cost,
        "profit": profit,
        "status": status,
        "status_color": status_color
    }


def build_result_text(name, crop, district, acres, risk, result):
    return f"""HARVEST HELP PROJECTION FOR {name.upper()}
------------------------------------------
Location: {district}
Crop: {crop} ({acres} acres)
Risk Level: {risk}

FINANCIAL SUMMARY:
- Expected Yield: {result['expected_yield']:,.1f} kg
- Total Revenue: {format_currency(result['revenue'])}
- Total Cost: {format_currency(result['total_cost'])}
- Projected Profit: {format_currency(result['profit'])}

STATUS: {result['status']}
"""


class HarvestHelpApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HarvestHelp SL - Farmer Projection Tool")
        self.root.geometry("900x700")
        self.root.configure(bg=PAPER)

        self.entries = {}
        self.summary_labels = {}
        self.records = []

        self.setup_ui()

    def setup_ui(self):
        # Header
        header = tk.Frame(self.root, bg=PRIMARY, pady=20)
        header.pack(fill="x")
        tk.Label(header, text="HARVESTHELP SL", fg="white", bg=PRIMARY, font=("Tahoma", 18, "bold")).pack()

        main_container = tk.Frame(self.root, bg=PAPER, padx=20, pady=20)
        main_container.pack(fill="both", expand=True)

        # Left Panel: Input
        left_panel = tk.Frame(main_container, bg=PAPER)
        left_panel.pack(side="left", fill="both", expand=True)

        tk.Label(left_panel, text="Farmer Details", bg=PAPER, fg=PRIMARY, font=("Tahoma", 12, "bold")).grid(row=0,
                                                                                                            column=0,
                                                                                                            columnspan=2,
                                                                                                            sticky="w",
                                                                                                            pady=(0,
                                                                                                                  10))

        self.add_text_entry(left_panel, "Farmer name", 1)
        self.add_combo(left_panel, "Crop", list(CROP_DATA.keys()), 2)
        self.add_text_entry(left_panel, "District", 3)
        self.add_combo(left_panel, "Risk level", ["Low", "Medium", "High"], 4)
        self.add_text_entry(left_panel, "Land size (acres)", 5)
        self.add_text_entry(left_panel, "Seed cost (SLE)", 6)
        self.add_text_entry(left_panel, "Fertilizer cost (SLE)", 7)
        self.add_text_entry(left_panel, "Labor cost (SLE)", 8)
        self.add_text_entry(left_panel, "Expected price per kg", 9)

        # Buttons
        btn_frame = tk.Frame(left_panel, bg=PAPER, pady=20)
        btn_frame.grid(row=10, column=0, columnspan=2, sticky="ew")
        self.add_button(btn_frame, "Calculate", self.calculate, "#3182CE", 0)
        self.add_button(btn_frame, "Clear", self.clear, "#718096", 1)
        self.add_button(btn_frame, "Load Demo", self.load_demo, "#38A169", 2)
        self.add_button(btn_frame, "Save CSV", self.save_csv, "#D69E2E", 3)

        # Right Panel: Results
        right_panel = tk.Frame(main_container, bg=PAPER, padx=20)
        right_panel.pack(side="right", fill="both", expand=True)

        # Summary Cards
        summary_frame = tk.Frame(right_panel, bg=PAPER)
        summary_frame.pack(fill="x")

        self.create_summary_card(summary_frame, "revenue", "REVENUE", PRIMARY, 0, 0)
        self.create_summary_card(summary_frame, "cost", "TOTAL COST", PRIMARY, 0, 1)
        self.create_summary_card(summary_frame, "profit", "PROFIT", PRIMARY, 1, 0)
        self.create_summary_card(summary_frame, "yield", "EXPECTED YIELD", PRIMARY, 1, 1)

        # Status Badge
        self.status_badge = tk.Label(right_panel, text="Waiting for input", bg=LINE, fg=INK,
                                     font=("Tahoma", 10, "bold"), pady=10)
        self.status_badge.pack(fill="x", pady=10)

        # Output Box
        self.output_box = tk.Text(right_panel, height=10, font=("Courier New", 10), bg=MINT, fg=INK, relief="solid",
                                  bd=1)
        self.output_box.pack(fill="both", expand=True)

        # History Table
        history_label = tk.Label(self.root, text="Calculation History", bg=PAPER, fg=PRIMARY,
                                 font=("Tahoma", 10, "bold"))
        history_label.pack(pady=(10, 0))

        self.history = ttk.Treeview(self.root, columns=("name", "crop", "district", "profit", "status"),
                                    show="headings", height=5)
        self.history.heading("name", text="Farmer")
        self.history.heading("crop", text="Crop")
        self.history.heading("district", text="District")
        self.history.heading("profit", text="Profit")
        self.history.heading("status", text="Status")
        self.history.pack(fill="x", padx=20, pady=(0, 20))

    def create_summary_card(self, parent, key, label, color, row, col):
        card = tk.Frame(parent, bg=PAPER, highlightbackground=LINE, highlightthickness=1, padx=10, pady=5)
        card.grid(row=row, column=col, sticky="ew", padx=5, pady=5)
        parent.columnconfigure(col, weight=1)

        tk.Label(card, text=label, bg=PAPER, fg=MUTED, font=("Tahoma", 9, "bold")).pack(anchor="w", padx=14,
                                                                                        pady=(8, 0))
        value = tk.Label(card, text="--", bg=PAPER, fg=color, font=("Tahoma", 15, "bold"))
        value.pack(anchor="w", padx=14, pady=(2, 8))
        self.summary_labels[key] = value

    def add_text_entry(self, parent, label, row):
        tk.Label(parent, text=label, bg=PAPER, fg=INK, font=("Tahoma", 10)).grid(row=row, column=0, sticky="w", padx=20,
                                                                                 pady=6)
        entry = tk.Entry(parent, width=25, font=("Tahoma", 10), bg=MINT, fg=INK, relief="solid", bd=1)
        entry.grid(row=row, column=1, sticky="ew", padx=(10, 20), pady=6, ipady=5)
        self.entries[label] = entry

    def add_combo(self, parent, label, values, row):
        tk.Label(parent, text=label, bg=PAPER, fg=INK, font=("Tahoma", 10)).grid(row=row, column=0, sticky="w", padx=20,
                                                                                 pady=6)
        combo = ttk.Combobox(parent, values=values, state="readonly", width=23, font=("Tahoma", 10))
        if values:
            combo.current(0)
        combo.grid(row=row, column=1, sticky="ew", padx=(10, 20), pady=6, ipady=3)
        self.entries[label] = combo

    def add_button(self, parent, label, command, bg, column, fg="white"):
        button = tk.Button(parent, text=label, command=command, bg=bg, fg=fg, activebackground=bg, activeforeground=fg,
                           font=("Tahoma", 9, "bold"), relief="flat", width=10, pady=7)
        button.grid(row=0, column=column, padx=4, sticky="ew")
        parent.columnconfigure(column, weight=1)

    def collect_inputs(self):
        name = self.entries["Farmer name"].get().strip()
        if not name:
            raise ValueError("Farmer name is required.")
        crop = self.entries["Crop"].get()
        district = self.entries["District"].get()
        risk = self.entries["Risk level"].get()
        acres = safe_float(self.entries["Land size (acres)"].get(), "Land size")
        seed_cost = safe_float(self.entries["Seed cost (SLE)"].get(), "Seed cost")
        fertilizer_cost = safe_float(self.entries["Fertilizer cost (SLE)"].get(), "Fertilizer cost")
        labor_cost = safe_float(self.entries["Labor cost (SLE)"].get(), "Labor cost")
        price = safe_float(self.entries["Expected price per kg"].get(), "Expected price")
        if acres == 0:
            raise ValueError("Land size must be greater than zero.")
        return name, crop, district, acres, seed_cost, fertilizer_cost, labor_cost, price, risk

    def calculate(self):
        try:
            name, crop, district, acres, seed_cost, fertilizer_cost, labor_cost, price, risk = self.collect_inputs()
            result = calculate_projection(crop, district, acres, seed_cost, fertilizer_cost, labor_cost, price, risk)
            display = build_result_text(name, crop, district, acres, risk, result)
            self.output_box.delete("1.0", "end")
            self.output_box.insert("1.0", display)
            self.update_summary(result)
            self.status_badge.configure(text=result["status"], bg=result["status_color"], fg="white")
            self.add_record(name, district, crop, acres, risk, result)
        except ValueError as error:
            messagebox.showerror("Input Error", str(error))

    def update_summary(self, result):
        self.summary_labels["revenue"].configure(text=format_currency(result["revenue"]))
        self.summary_labels["cost"].configure(text=format_currency(result["total_cost"]))
        self.summary_labels["profit"].configure(text=format_currency(result["profit"]),
                                                fg=PRIMARY if result["profit"] >= 0 else RED)
        self.summary_labels["yield"].configure(text=f"{result['expected_yield']:,.1f} kg")

    def add_record(self, name, district, crop, acres, risk, result):
        record = {
            "farmer": name,
            "district": district,
            "crop": crop,
            "acres": acres,
            "risk": risk,
            "yield": result["expected_yield"],
            "revenue": result["revenue"],
            "cost": result["total_cost"],
            "profit": result["profit"],
            "status": result["status"],
        }
        self.records.append(record)
        self.history.insert("", "end",
                            values=(name, crop, district, format_currency(result["profit"]), result["status"]))

    def load_demo(self):
        for label, value in DEMO_VALUES.items():
            widget = self.entries.get(label)
            if widget:
                if isinstance(widget, ttk.Combobox):
                    widget.set(value)
                else:
                    widget.delete(0, "end")
                    widget.insert(0, value)

    def clear(self):
        for widget in self.entries.values():
            if isinstance(widget, ttk.Combobox):
                widget.current(0)
            else:
                widget.delete(0, "end")
        self.output_box.delete("1.0", "end")
        self.output_box.insert("1.0", "Input cleared. Enter new farm details.")
        self.status_badge.configure(text="Waiting for input", bg=LINE, fg=INK)
        for label in self.summary_labels.values():
            label.configure(text="--")

    def save_csv(self):
        if not self.records:
            messagebox.showinfo("No Records", "Please calculate at least one record before saving.")
            return
        try:
            with EXPORT_FILE.open("w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(
                    ["Farmer", "District", "Crop", "Acres", "Risk", "YieldKg", "Revenue", "Cost", "Profit", "Status"])
                for record in self.records:
                    writer.writerow([
                        record["farmer"],
                        record["district"],
                        record["crop"],
                        record["acres"],
                        record["risk"],
                        f"{record['yield']:.2f}",
                        f"{record['revenue']:.2f}",
                        f"{record['cost']:.2f}",
                        f"{record['profit']:.2f}",
                        record["status"],
                    ])
            messagebox.showinfo("Saved", f"Records saved to {EXPORT_FILE.resolve()}")
        except Exception as e:
            messagebox.showerror("Save Error", f"Could not save file: {e}")

    def build_crop_guide(self):
        lines = ["HARVESTHELP SL CROP GUIDE", "",
                 "Use this tab during presentation to explain how the system supports farm decisions.", ""]
        for crop, data in CROP_DATA.items():
            lines.append(f"{crop}")
            lines.append(f"  Yield per acre: {data['yield_per_acre']:,} kg")
            lines.append(f"  Seed per acre: {data['seed_kg']} kg")
            lines.append(f"  Best season: {data['season']}")
            lines.append(f"  Water need: {data['water_need']}")
            lines.append(f"  Advice: {data['advice']}")
            lines.append("")
        lines.append(
            "Structured programming shown: variables, constants, dictionaries, functions, decisions, loops, input validation, GUI and file export.")
        return "\n".join(lines)


def main():
    root = tk.Tk()
    app = HarvestHelpApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
