// ============================================================
// 📦 ETAPA 1: Definição das Models Base
// ============================================================

interface ICategory {
  id: number;
  name: string;
}

interface IProduct {
  id: number;
  name: string;
  price: number;
  category: ICategory;
}

class Category implements ICategory {
  constructor(
    public id: number,
    public name: string
  ) {}
}

class Product implements IProduct {
  constructor(
    public id: number,
    public name: string,
    public price: number,
    public category: ICategory
  ) {}
}

// ============================================================
// 👤 ETAPA 2: Gerenciamento de Usuários (Roles)
// ============================================================

// Opção com Enum (mais robusto e auto-documentado)
enum UserRole {
  ADMIN = "ADMIN",
  CUSTOMER = "CUSTOMER",
}

// Opção com Literal Type (alternativa enxuta)
type UserRoleLiteral = "ADMIN" | "CUSTOMER";

interface IUser {
  id: number;
  username: string;
  email: string;
  role: UserRole;
}

class User implements IUser {
  constructor(
    public id: number,
    public username: string,
    public email: string,
    public role: UserRole
  ) {}

  isAdmin(): boolean {
    return this.role === UserRole.ADMIN;
  }
}

// ============================================================
// 🛒 ETAPA 3: Lógica do Carrinho (Cart)
// ============================================================

interface CartItem {
  product: IProduct;
  quantity: number;
}

class Cart {
  private items: CartItem[] = [];

  constructor(public owner: User) {}

  addItem(product: IProduct, quantity: number): void {
    const existing = this.items.find((i) => i.product.id === product.id);
    if (existing) {
      existing.quantity += quantity;
    } else {
      this.items.push({ product, quantity });
    }
  }

  removeItem(productId: number): void {
    this.items = this.items.filter((i) => i.product.id !== productId);
  }

  getItems(): CartItem[] {
    return this.items;
  }

  /** Retorna a quantidade total de unidades (soma das quantidades) no carrinho */
  getTotalItems(): number {
    return this.items.reduce((sum, item) => sum + item.quantity, 0);
  }

  /** Retorna o valor monetário total da compra */
  getFinalPrice(): number {
    return this.items.reduce(
      (total, item) => total + item.product.price * item.quantity,
      0
    );
  }

  clear(): void {
    this.items = [];
  }
}

// ============================================================
// 🧪 Exemplo de uso
// ============================================================

const electronics = new Category(1, "Eletrônicos");
const clothing = new Category(2, "Roupas");

const notebook = new Product(101, "Notebook Pro 15", 4599.9, electronics);
const headphone = new Product(102, "Headphone Bluetooth", 349.9, electronics);
const tshirt = new Product(201, "Camiseta Dev", 89.9, clothing);

const admin = new User(1, "ana_admin", "ana@loja.com", UserRole.ADMIN);
const customer = new User(2, "joao_customer", "joao@email.com", UserRole.CUSTOMER);

const cart = new Cart(customer);
cart.addItem(notebook, 1);
cart.addItem(headphone, 2);
cart.addItem(tshirt, 3);

console.log("=== RESUMO DO CARRINHO ===");
console.log(`Dono: ${cart.owner.username} (${cart.owner.role})`);
console.log(`Total de itens (unidades): ${cart.getTotalItems()}`);
console.log(`Preço final: R$ ${cart.getFinalPrice().toFixed(2)}`);
console.log("Itens:", cart.getItems().map(i => `${i.product.name} x${i.quantity}`));
