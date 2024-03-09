"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.AuthorizationService = void 0;
const common_1 = require("@nestjs/common");
const crypto = __importStar(require("crypto"));
const qs = __importStar(require("qs"));
const errors_1 = require("../errors");
let AuthorizationService = class AuthorizationService {
    async isSlackRequest(request) {
        // Validating that the request was send from slack.
        const slackSigningSecret = process.env["SLACK_SIGNING_SECRET"] ?? "";
        const slackSignature = request.headers["x-slack-signature"] ?? "";
        const requestBody = qs.stringify(request.body, { format: "RFC1738" });
        const timestamp = request.headers["x-slack-request-timestamp"] ?? 0;
        if (!timestamp || !slackSignature) {
            this.throwUnauthorized();
        }
        const time = Math.floor(new Date().getTime() / 1000);
        // Ignore request if its older than 5 min.
        if (Math.abs(time - parseInt(timestamp.toString())) > 300) {
            this.throwUnauthorized();
        }
        // Create my signature with request data and slackSigningSecret
        const sigBasestring = "v0:" + timestamp + ":" + requestBody;
        const mySignature = "v0=" +
            crypto
                .createHmac("sha256", slackSigningSecret)
                .update(sigBasestring, "utf8")
                .digest("hex");
        // Compare my signature with x-slack-signature
        if (!crypto.timingSafeEqual(Buffer.from(mySignature, "utf8"), Buffer.from(slackSignature.toString(), "utf8"))) {
            this.throwUnauthorized();
        }
    }
    throwUnauthorized() {
        throw new errors_1.UnauthorizedError("You are not allowed to call this endpoint");
    }
};
exports.AuthorizationService = AuthorizationService;
exports.AuthorizationService = AuthorizationService = __decorate([
    (0, common_1.Injectable)()
], AuthorizationService);
//# sourceMappingURL=authorization.service.js.map